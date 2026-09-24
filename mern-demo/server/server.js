require('dotenv').config();
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));

const StudentSchema = new mongoose.Schema({
  studentId: String,
  name: String,
  email: String
});
const Student = mongoose.model('Student', StudentSchema);

app.get('/api/hello', (req, res) => {
  res.json({ message: "Backend is running!" });
});

app.get('/api/students', async (req, res) => {
  const students = await Student.find();
  res.json(students);
});

app.post('/api/students', async (req, res) => {
  const student = await Student.create(req.body);
  res.json(student);
});

app.put('/api/students/:id', async (req, res) => {
  const student = await Student.findByIdAndUpdate(req.params.id, req.body, {new:true});
  res.json(student);
});

app.delete('/api/students/:id', async (req, res) => {
  await Student.findByIdAndDelete(req.params.id);
  res.json({ message: "Deleted" });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
