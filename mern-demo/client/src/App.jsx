import React, { useEffect, useState } from 'react';

function App() {
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState({ studentId: '', name: '', email: '' });
  const [editingId, setEditingId] = useState(null);

  const API_URL = 'http://localhost:5000/api/students';

  const loadStudents = () => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setStudents(data))
      .catch(err => console.error(err));
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
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Quản lý sinh viên</h1>
      <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
        <input 
          placeholder="MSSV" 
          value={form.studentId} 
          onChange={e => setForm({...form, studentId: e.target.value})} 
          required 
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <input 
          placeholder="Họ tên" 
          value={form.name} 
          onChange={e => setForm({...form, name: e.target.value})} 
          required 
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <input 
          placeholder="Email" 
          type="email"
          value={form.email} 
          onChange={e => setForm({...form, email: e.target.value})} 
          required 
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <button type="submit" style={{ padding: '5px 10px', cursor: 'pointer' }}>
          {editingId ? 'Cập nhật' : 'Thêm'}
        </button>
        {editingId && (
          <button 
            type="button" 
            onClick={() => { setEditingId(null); setForm({ studentId: '', name: '', email: '' }); }}
            style={{ marginLeft: '10px', padding: '5px 10px', cursor: 'pointer' }}
          >
            Hủy
          </button>
        )}
      </form>
      
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {students.map(s => (
          <li key={s._id} style={{ marginBottom: '10px', padding: '10px', border: '1px solid #ccc' }}>
            <strong>{s.studentId}</strong> - {s.name} - {s.email}
            <button 
              onClick={() => handleEdit(s)} 
              style={{ marginLeft: '15px', padding: '3px 8px', cursor: 'pointer' }}
            >
              Sửa
            </button>
            <button 
              onClick={() => handleDelete(s._id)} 
              style={{ marginLeft: '5px', padding: '3px 8px', cursor: 'pointer', color: 'red' }}
            >
              Xóa
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
