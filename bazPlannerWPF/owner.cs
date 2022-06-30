using static bazPlannerWPF.sqlite_connect;

namespace bazPlannerWPF
{
    public class Owner
    {
        public string nameOwner;
        public string passwordOwner;

        public void AddToDatabase(string nameOwner, string passwordOwner)
        {
            InsertUser(nameOwner, passwordOwner);
        }
    }
}
