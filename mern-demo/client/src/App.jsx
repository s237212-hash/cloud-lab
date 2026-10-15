import React, { useEffect, useState } from 'react';

function App() {
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState({ studentId: '', name: '', email: '' });
  const [editingId, setEditingId] = useState(null);

  const API_BASE = import.meta.env.VITE_API_URL || 
    (typeof window !== 'undefined' && window.location.hostname !== 'localhost' 
      ? 'https://mern-backend-tien.onrender.com' 
      : '');
  const API_URL = API_BASE ? `${API_BASE}/api/students` : '/api/students';

  const loadStudents = () => {
    fetch(API_URL)
      .then(res => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then(data => {
        if (Array.isArray(data)) {
          setStudents(data);
        } else {
          console.error('Expected array, got:', data);
        }
      })
      .catch(err => console.error('Lỗi tải danh sách sinh viên:', err));
  };

  useEffect(() => {
    loadStudents();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingId) {
      // Cập nhật sinh viên (PUT)
      fetch(`${API_URL}/${editingId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      }).then(() => {
        loadStudents();
        setForm({ studentId: '', name: '', email: '' });
        setEditingId(null);
      }).catch(err => console.error(err));
    } else {
      // Thêm sinh viên (POST)
      fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      }).then(() => {
        loadStudents();
        setForm({ studentId: '', name: '', email: '' });
      }).catch(err => console.error(err));
    }
  };

  const handleEdit = (student) => {
    setForm({ studentId: student.studentId, name: student.name, email: student.email });
    setEditingId(student._id);
  };

  const handleDelete = (id) => {
    if (window.confirm('Bạn có chắc chắn muốn xoá sinh viên này?')) {
      // Xoá sinh viên (DELETE)
      fetch(`${API_URL}/${id}`, {
        method: 'DELETE'
      }).then(() => {
        loadStudents();
      }).catch(err => console.error(err));
    }
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', maxWidth: '900px', margin: '0 auto' }}>
      <h1 style={{ textAlign: 'center', color: '#1a1a1a', marginBottom: '25px', fontSize: '28px', fontWeight: 'bold' }}>
        Quản Lý Sinh Viên Version 2.0
      </h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: '30px', display: 'flex', gap: '10px', flexWrap: 'wrap', justifyContent: 'center' }}>
        <input 
          placeholder="MSSV" 
          value={form.studentId} 
          onChange={e => setForm({...form, studentId: e.target.value})} 
          required 
          style={{ padding: '8px 12px', border: '1px solid #ccc', borderRadius: '4px', minWidth: '150px' }}
        />
        <input 
          placeholder="Họ tên" 
          value={form.name} 
          onChange={e => setForm({...form, name: e.target.value})} 
          required 
          style={{ padding: '8px 12px', border: '1px solid #ccc', borderRadius: '4px', minWidth: '200px' }}
        />
        <input 
          placeholder="Email" 
          type="email"
          value={form.email} 
          onChange={e => setForm({...form, email: e.target.value})} 
          required 
          style={{ padding: '8px 12px', border: '1px solid #ccc', borderRadius: '4px', minWidth: '220px' }}
        />
        <button 
          type="submit" 
          style={{ padding: '8px 18px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
        >
          {editingId ? 'Cập nhật' : 'Thêm'}
        </button>
        {editingId && (
          <button 
            type="button" 
            onClick={() => { setEditingId(null); setForm({ studentId: '', name: '', email: '' }); }}
            style={{ padding: '8px 15px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
          >
            Hủy
          </button>
        )}
      </form>
      
      <h2 style={{ textAlign: 'center', color: '#333', marginBottom: '15px', fontSize: '22px', fontWeight: 'bold' }}>
        Danh Sách Sinh Viên
      </h2>

      <table style={{ width: '100%', borderCollapse: 'collapse', border: '1px solid #d1d5db', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
        <thead>
          <tr style={{ backgroundColor: '#f3f4f6' }}>
            <th style={{ padding: '12px', border: '1px solid #d1d5db', textAlign: 'center', color: '#4b5563', fontWeight: 'bold' }}>MSSV</th>
            <th style={{ padding: '12px', border: '1px solid #d1d5db', textAlign: 'center', color: '#4b5563', fontWeight: 'bold' }}>Họ và Tên</th>
            <th style={{ padding: '12px', border: '1px solid #d1d5db', textAlign: 'center', color: '#4b5563', fontWeight: 'bold' }}>Email</th>
            <th style={{ padding: '12px', border: '1px solid #d1d5db', textAlign: 'center', color: '#4b5563', fontWeight: 'bold' }}>Thao Tác</th>
          </tr>
        </thead>
        <tbody>
          {students.length > 0 ? (
            students.map((s, index) => (
              <tr key={s._id || index} style={{ backgroundColor: index % 2 === 0 ? '#ffffff' : '#f9fafb' }}>
                <td style={{ padding: '10px 12px', border: '1px solid #d1d5db', textAlign: 'center', fontWeight: '500' }}>{s.studentId}</td>
                <td style={{ padding: '10px 12px', border: '1px solid #d1d5db' }}>{s.name}</td>
                <td style={{ padding: '10px 12px', border: '1px solid #d1d5db' }}>{s.email}</td>
                <td style={{ padding: '10px 12px', border: '1px solid #d1d5db', textAlign: 'center' }}>
                  <button 
                    onClick={() => handleEdit(s)} 
                    style={{ padding: '5px 12px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', marginRight: '6px' }}
                  >
                    Sửa
                  </button>
                  <button 
                    onClick={() => handleDelete(s._id)} 
                    style={{ padding: '5px 12px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
                  >
                    Xóa
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" style={{ padding: '20px', textAlign: 'center', color: '#888', border: '1px solid #d1d5db' }}>
                Đang tải dữ liệu từ máy chủ hoặc chưa có sinh viên nào...
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
