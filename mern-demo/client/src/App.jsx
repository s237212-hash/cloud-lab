import React, { useEffect, useState } from 'react';

function App() {
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState({ studentId: '', name: '', email: '' });

  useEffect(() => {
    fetch('/api/students')
      .then(res => res.json())
      .then(data => setStudents(data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/api/students', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    }).then(() => window.location.reload());
  };

  return (
    <div>
      <h1>Quản lý sinh viên</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="MSSV" onChange={e => setForm({...form, studentId: e.target.value})} />
        <input placeholder="Họ tên" onChange={e => setForm({...form, name: e.target.value})} />
        <input placeholder="Email" onChange={e => setForm({...form, email: e.target.value})} />
        <button type="submit">Thêm</button>
      </form>
      <ul>
        {students.map(s => <li key={s._id}>{s.studentId} - {s.name} - {s.email}</li>)}
      </ul>
    </div>
  );
}

export default App;
