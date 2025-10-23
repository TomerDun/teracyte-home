import { Route, Routes } from "react-router";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";

export default function Routing() {
    return (
        <Routes>
            <Route path='/login' element={<LoginPage />} />
            <Route path='/images/:selectedImageId' element={<HomePage />} />
            <Route path='/' element={<HomePage />} />
        </Routes>
    )
}