namespace bazPlannerTests
{
    [TestClass]
    public class DatabaseTest
    {
        [TestMethod]
        public void ConnectTest()
        {
            string nameDatabase = "test.db";
            string expected = "test.db";
            
            bazPlanner.Models.Database.Connect(nameDatabase);

            Assert.AreEqual(expected, nameDatabase);
        }

        [TestMethod]
        public void ConnectTest2()
        {
            string nameDatabase = "test.db";
            string expected = "test.db";

            bazPlanner.Models.Database.Connect(nameDatabase);

            Assert.AreEqual(expected, nameDatabase);
        }

        [TestMethod]
        public void SelectOwner_1()
        {
            string login = "admin2";
            string password = "admin2";
            int expected = 1;

            int actual = bazPlanner.Models.Database.SelectOwner(login, password);

            Assert.AreEqual(expected,actual);
        }

        [TestMethod]
        public void SelectOwner_2()
        {
            string login = "admin";
            string password = "admin";
            int expected = 1;

            int actual = bazPlanner.Models.Database.SelectOwner(login, password);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SelectOwner_3()
        {
            string login = "admin3";
            string password = "admin3";
            int expected = 1;

            int actual = bazPlanner.Models.Database.SelectOwner(login, password);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void InsertProject_1()
        {
            string projectName = "name_name_name123";
            string projectOwner = "admin";
            bool expected = true;

            bool actual = bazPlanner.Models.Database.InsertProject(projectName, projectOwner);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void InsertProject_2()
        {
            string projectName = "name_name_name098765";
            string projectOwner = "admin2";
            bool expected = true;

            bool actual = bazPlanner.Models.Database.InsertProject(projectName, projectOwner);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void InsertProject_3()
        {
            string projectName = "QWERTY_name_name_name";
            string projectOwner = "admin3";
            bool expected = true;

            bool actual = bazPlanner.Models.Database.InsertProject(projectName, projectOwner);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void InsertProject_4()
        {
            string projectName = "name_name_name123_QWERTY123";
            string projectOwner = "admin3";
            bool expected = true;

            bool actual = bazPlanner.Models.Database.InsertProject(projectName, projectOwner);

            Assert.AreEqual(expected, actual);
        }
    }
}